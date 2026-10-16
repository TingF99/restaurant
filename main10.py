"""使用鏈結法處理雜湊表碰撞。"""

BUCKET_COUNT = 13
VALUE_COUNT = 15


def build_hash_table(values):
    """依照 value % 13 將數值放入對應的鏈結串列。"""
    buckets = [[] for _ in range(BUCKET_COUNT)]
    for value in values:
        buckets[value % BUCKET_COUNT].append(value)
    return buckets


def read_values():
    """讀取一行以空格或逗號分隔的 15 個整數。"""
    while True:
        raw_values = input(
            f"請輸入 {VALUE_COUNT} 個整數（以空格或逗號分隔）："
        ).strip()
        tokens = raw_values.replace(",", " ").split()

        if len(tokens) != VALUE_COUNT:
            print(f"輸入數量錯誤，請輸入剛好 {VALUE_COUNT} 個整數。")
            continue

        try:
            return [int(token) for token in tokens]
        except ValueError:
            print("輸入內容包含非整數，請重新輸入。")


def display_hash_table(values, buckets):
    print("\n=== 雜湊位置（雜湊函數：數值 % 13）===")
    for value in values:
        print(f"{value} % {BUCKET_COUNT} = {value % BUCKET_COUNT}")

    print("\n=== 雜湊表（鏈結法）===")
    for index, bucket in enumerate(buckets):
        chain = " -> ".join(str(value) for value in bucket) or "空"
        print(f"{index:2}: {chain}")


def main():
    print("=== 雜湊表：除 13 取餘數與鏈結法 ===")
    values = read_values()
    buckets = build_hash_table(values)
    display_hash_table(values, buckets)


if __name__ == "__main__":
    main()