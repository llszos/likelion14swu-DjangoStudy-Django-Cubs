def is_valid_input(name):
    return name.strip() != ""


print("🦁 아기 사자 명단 관리 프로그램입니다.")

lions = []

while True:
    name = input("✏️  아기 사자 이름을 입력하세요 (종료하려면 q 입력): ")

    if name == "q":
        print("\n📌 이름 입력을 종료합니다.")
        break

    if not is_valid_input(name):
        print("⚠️  이름이 비어있습니다. 다시 입력해주세요.")
        continue
        
		# lion 리스트에 등록
    lions.append(name)
    print(f"✅ '{name}' 이(가) 등록되었습니다.")

print("\n📋 현재 아기 사자 명단입니다.")

for i in range(len(lions)):
    print(f"🦁 {i+1}. {lions[i]}")