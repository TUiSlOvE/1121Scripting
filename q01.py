from pkg.modu import triangle_zhonxin

print("請輸入三角形的 3 個頂點坐標")
print("------------------------------")

a = tuple(map(int, input("請輸入頂點 a 的坐標：").split(',')) )
b = tuple(map(int, input("請輸入頂點 b 的坐標：").split(',')) )
c = tuple(map(int, input("請輸入頂點 c 的坐標：").split(',')) )

print("------------------------------")

result = triangle_zhonxin(a, b, c)
print(f"此三角形的重心為：{result}")
