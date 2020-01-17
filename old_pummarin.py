import hashlib
import json
# เสแสร้ง block ที่ยังไม่ได้พิสูจน์
blocks = [
    {
        'block_id': 0,
        'block_hash': None,
        'prev_hash': None,
        'transactions': {
            'tx': 10
        }
    },
    {
        'block_id': 1,
        'block_hash': None,
        'prev_hash': None,
        'transactions': {
            'tx': 20
        }
    },
    {
        'block_id': 2,
        'block_hash': None,
        'prev_hash': None,
        'transactions': {
            'tx': 30
        }
    }

]

# blockchains เป็นเชนที่เก็บบล็อคที่พิสูจน์แล้ว
blockchains = []

# ฟังชั่นการต่อ blockchain


def hashblock(block, prev_hash):
    # ถ้าเป็น Genesis Block ให้ hash ตัวเองเป็น prev_hash แล้ว hash ตัวเองอีกครั้งเป็น block_hash (hashของblockนั้น)
    if prev_hash is None:
        block_ordered = json.dumps(block, sort_keys=True).encode('utf-8')
        block['prev_hash'] = hashlib.sha256(
            block_ordered).hexdigest()
        block_ordered = json.dumps(block, sort_keys=True).encode('utf-8')
        block['block_hash'] = hashlib.sha256(
            block_ordered).hexdigest()  # hash block ตัวเอง
    else:
        block['prev_hash'] = prev_hash  # เก็บค่า prev_hash ตัวก่อนหน้า
        block_ordered = json.dumps(block, sort_keys=True).encode('utf-8')
        block['block_hash'] = hashlib.sha256(
            block_ordered).hexdigest()  # hash block ตัวเอง

    return block


def hash_blocks(blocks):
    prev_hash = blocks[0]['prev_hash']
    for block in blocks:
        block['prev_hash'] = prev_hash
        block_serialized = json.dumps(block, sort_keys=True).encode('utf-8')
        block_hash = hashlib.sha256(block_serialized).hexdigest()
        prev_hash = block_hash
    return prev_hash


# ทำการต่อ block เข้าสู่ chains แท้
for i in range(len(blocks)):
    if blocks[i]['prev_hash'] is None:
        b = hashblock(blocks[i], None)
        blockchains.append(b)
        blocks[i+1]['prev_hash'] = b['block_hash']  # เรียกบล็อคถัดไปยังไง..
    elif i+1 == len(blocks):
        b = hashblock(blocks[i], blocks[i]['prev_hash'])
        blockchains.append(b)
    else:
        b = hashblock(blocks[i], blocks[i]['prev_hash'])
        blockchains.append(b)
        blocks[i+1]['prev_hash'] = b['block_hash']
# แสดงรายละเอียด chains แท้
for i, block in enumerate(blockchains):
    print("Block {}:\nblock_id: {}\nblock_hash: {}\nprev_hash: {}\ntransactions: {}\n\n".format(
        i, block['block_id'], block['block_hash'], block['prev_hash'], block['transactions']))

hash_blockchains = hash_blocks(blockchains)  # TODO: false here!
# print("\n\nblockchains = ", blockchains, "\n\n")  # debug OK
print("Hashed of all blockchains = {}".format(hash_blockchains))

# ===============================================================================================
# เลือกบล็อคที่ต้องการเปลี่ยนแปลงข้อมูล
selectBlock = int(input("Choose the block you want to modify(0-2): "))
val = int(input("Enter value: "))
# ทำการเปลี่ยนแปลงข้อมูลในบล็อคแท้
# tmp = blockchains[selectBlock]['block_hash']  # สำรอง
blockchains[selectBlock]['transactions']['tx'] = val
print("blockchains after mofify:", blockchains, "\n\n")
# เมื่อทำการเปลี่ยนแปลงข้อมูลแล้ว ค่าแฮชของบล็อคนั้นต้องเปลี่ยน
blockchains[selectBlock] = hashblock(
    blockchains[selectBlock], blockchains[selectBlock]['prev_hash'])
print("blockchains specific block:", blockchains[selectBlock])
new_hash_blockchains = hash_blocks(blockchains)
if new_hash_blockchains != hash_blockchains:
    print("Block {} have been modify!".format(selectBlock))
    print("Old hashed all block: {}\nNew hashed all block: {}\n".format(
        hash_blockchains, new_hash_blockchains))
else:
    print("BlockChains is OK.")
