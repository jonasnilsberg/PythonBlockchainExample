import block

blockchain = []
blockchain.append(block.create_genesis_block())
last_block = blockchain[0]
num_of_blocks = 10

for i in range(0, num_of_blocks):
    block_to_add = block.next_block(last_block)
    blockchain.append(block_to_add)
    last_block = block_to_add

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
