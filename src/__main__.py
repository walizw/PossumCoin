from .chain import Chain

chain = Chain()
chain.add_block("one")
chain.add_block("two")
chain.add_block("three")

print(chain)
