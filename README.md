# Fastest way to create Short Id

## How we create short id

Under writing

## Installation

Open your terminal and run:

```shell
pip install shrt_id
```

Then, at the top of each of your Python script, you should be able to import the module:

```python
from shrt_id import ShortId
```

## Use shrt_id

Simple use

```python
id = ShortId().id()
print(id)
# ev60bb7Q (default length is 8)
```

Custom length

```python
id = ShortId().id(10)
print(id)
# wiwdhx8V7x
```

Get Id and shard at same time

```python
id, shard = ShortId().id_with_shard(10)
print(id, shard)
# ev60fM2z89
```

Decode id for datetime and shard

```python
id, shard = ShortId().id_with_shard()
print(id, shard)
# ev60rHdz 31
decoded_id = ShortId().decode(id)
print(decoded_id)
# {'shard_seq': 31, 'dt': datetime.datetime(2022, 8, 22, 17, 37, 18, 300000), 'random_string': 'dz', 'random_seq': 211}
```

## Thanks
