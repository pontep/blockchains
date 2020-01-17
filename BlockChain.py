import hashlib
import json


class BlockChain:  # BlockChain class
    blockchains = []
    hashval = None
    last_block_hash = None
    length = 0
    genesis_block = {
        'block_id': None,
        'prev_hash': None,
        'block_hash': None,
        'transactions': {
            'tx1': 'generate genesis block.'
        }
    }

    def spacer1(self):
        print("*" * 80)

    def spacer2(self):
        print(" " * 80)

    def details(self):
        print("Block-chains Details")
        for block in self.blockchains:
            self.spacer2()
            print("BlockID: {}\nBlock hash: {}\nPrev Hash: {}\nTransactions: {}".format(
                block['block_id'], block['block_hash'], block['prev_hash'], block['transactions']))
        self.spacer2()

    # def BlockChain(self):
    #     self.generate_genesis_block()
    def check(self):
        count = 0
        for block in self.blockchains:
            _hash = block['block_hash']
            block['block_hash'] = None
            b = json.dumps(block, sort_keys=True).encode('utf-8')
            block['block_hash'] = hashlib.sha256(b).hexdigest()
            if _hash != block['block_hash']:
                self.spacer1()
                print("ALERT BLOCKCHAINS HAVE BEEN MODIFY AT BLOCK {}!".format(count))
                print("Original hash: {}\nNew hash: {}".format(
                    _hash, block['block_hash']))
                self.spacer1()
                return
            count += 1
        print("Block chain is secured.")

    def hack(self, n, val):
        tmp_hash = self.blockchains[n]['block_hash']
        self.blockchains[n]['transactions']['tx1'] = val
        # self.check()

    def alert(self, org, now):
        print("old value: {}\nnow value: {}\n".format(org, now))

    def generate_genesis_block(self):
        self.genesis_block['block_id'] = self.length
        self.length += 1
        b = json.dumps(self.genesis_block, sort_keys=True).encode('utf-8')
        self.genesis_block['prev_hash'] = hashlib.sha256(b).hexdigest()
        b = json.dumps(self.genesis_block, sort_keys=True).encode('utf-8')
        self.genesis_block['block_hash'] = hashlib.sha256(b).hexdigest()
        self.blockchains.append(self.genesis_block)
        self.last_block_hash = self.genesis_block['block_hash']
        print("Generating Genesis Block..........OK\n")

    def addblock(self, newblock):
        newblock['prev_hash'] = self.last_block_hash
        newblock['block_id'] = self.length
        self.length += 1
        b = json.dumps(newblock, sort_keys=True).encode('utf-8')
        newblock['block_hash'] = hashlib.sha256(b).hexdigest()
        self.blockchains.append(newblock)
        self.last_block_hash = newblock['block_hash']
        # print("Adding new Block: {}".format(newblock))
        print("Adding new block..........OK\n")
