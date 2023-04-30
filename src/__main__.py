from .blockchain.chain import Chain

chain = Chain()
for i in range(5):
    chain.add_block(i)

print(chain)
