def main():
    scores = {'陈': 94, '王': 92, '陆': 95}

    print(scores['陈'])
    print(scores['王'])

    # 遍历

    for ele in scores:
        print("%s\t -->\t%d" % (ele, scores[ele]))

    scores['邱'] = 94
    scores['李'] = 95
    scores.update(赵=96, 常=90)
    print(scores)

    if '孙' in scores:
        print(scores['孙'])

    print(scores.get('孙'))
    print(scores.get('孙', 91))

    # 删除
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('陈', 94))
    print(scores)

    # 清空字典
    scores.clear()
    print(scores)


if __name__ == "__main__":
    main()
