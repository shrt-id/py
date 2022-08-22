from datetime import datetime
import time
import string
import random

DEFALT_LENGTH = 8
alpha = string.ascii_letters + string.digits
alpha_len = len(alpha)


class ShortId:
    def __init__(self, shard: int = 60, start_date: datetime = datetime(2020, 1, 1)) -> None:
        self.start_timestamp_block = round(start_date.timestamp() * 10)
        self.shard = shard
        pass

    def number_to_string(self, number: int):
        output = ""
        while number:
            number, digit = divmod(number, alpha_len)
            output = alpha[digit] + output
        return output

    def string_from_timestamp(self):
        number = round(time.time() * 10) - self.start_timestamp_block
        return self.number_to_string(number=number)

    def random_shard(self):
        idx = random.randint(0, 60)
        return alpha[idx]

    def id(self, l: int = DEFALT_LENGTH):
        time_id = self.string_from_timestamp()
        shard_id = self.random_shard()
        rand_id_l = l - len(time_id) - 1
        rand_id = "".join(random.choices(alpha, k=rand_id_l))

        return "{}{}{}".format(time_id, rand_id, shard_id)
