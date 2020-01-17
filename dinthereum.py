import hashlib
import json
import testdata
import BlockChain

# Main
eth = BlockChain.BlockChain()
eth.generate_genesis_block()

eth.addblock(testdata.blocks[0])
eth.addblock(testdata.blocks[1])

eth.details()
eth.hack(1, 'HACKED')
eth.details()
eth.check()
