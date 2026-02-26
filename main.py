import random

def guess_number_game():
    print("歡迎來到猜數字遊戲！")
    print("我已經想好了一個 1 到 100 之間的數字。")
    
    # 電腦隨機產生一個 1 到 100 的數字
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("請輸入你猜的數字："))
            attempts += 1
            
            if guess < secret_number:
                print("太小了！再試一次。")
            elif guess > secret_number:
                print("太大了！再試一次。")
            else:
                print(f"恭喜你猜對了！答案就是 {secret_number}。")
                print(f"你總共猜了 {attempts} 次。")
                break
        except ValueError:
            print("請輸入有效的整數數字喔！")

if __name__ == "__main__":
    guess_number_game()
