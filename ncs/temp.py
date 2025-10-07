import multiprocessing

def increment(shared_number):
    """共有メモリ内の数値をインクリメントする"""
    with shared_number.get_lock():
        shared_number.value += 1

if __name__ == '__main__':
    # 共有メモリオブジェクトの作成
    shared_number = multiprocessing.Value('i', 0)  # 'i' は int 型を意味する
    
    # プロセスのリスト
    processes = []
    
    # 100個のプロセスを作成し、共有メモリの数値をインクリメント
    for _ in range(100):
        p = multiprocessing.Process(target=increment, args=(shared_number,))
        processes.append(p)
        p.start()
    
    # 全プロセスの終了を待つ
    for p in processes:
        p.join()
    
    print(f'Final value: {shared_number.value}')

