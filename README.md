对联数据集。

Also available on [HuggingFace](https://huggingface.co/datasets/wb14123/couplet).

This is a project to fetch couplets from [冯重朴_梨味斋散叶_的博客](http://blog.sina.com.cn/s/articlelist_1195052695_2_1.html)

This dataset contains more than 700,000 couplets.

Run the spider:
-------------

```
scrapy runspider sina_spider.py
```

It will store the data into `./output/`.


Download the data
-------------------

There is an already fetched and cleaned dataset that can be used directly with the seq2seq model. You can download it at [here](https://github.com/wb14123/couplet-dataset/releases/download/1.0/couplet.tar.gz).

The downloaded data contains 5 files:

1. `train/in.txt`: The input of the couplets. Each line is an input. Each word is split by space.
2. `train/out.txt`: The output of the couplets. Each line is the output for the same line in the `in.txt`. Each word is split by space.
3. `test/in.txt`: Same as `train/in.txt` but with less data.
4. `test/out.txt`: Same as `train/out.txt` but with less data.
5. `vocabs`: Vocabs file. Add `<s>` and `<\s>` as the first vocabs, which will be used to train in the seq2seq mode.

