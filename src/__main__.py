from .blockchain.chain import Chain

chain = Chain()
for i in range(2):
    chain.add_block(i)

print(chain)
