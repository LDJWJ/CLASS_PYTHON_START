# 연락처 프로그램 만들기

import time

class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)
        print("")

# 메뉴 출력 
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

# 연락처 입력 함수
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

# 연락처 출력
def print_contact(contact_list):
    len_num = len(contact_list)
    print(f"{len_num}개의 연락처")
    for contact in contact_list:
        contact.print_info()

# 연락처 삭제
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def run():
    contact_list = []

    menu = print_menu()
    print("메뉴 선택 :", menu)
    
    while (menu!=4):
        menu = print_menu()
        if menu == 1:
            c1 = set_contact()
            contact_list.append(c1)
            print("연락처 저장 완료")
            print(f"{len(contact_list)}개의 연락처 있습니다.")
            
        elif menu == 2:
            print_contact(contact_list)
            
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
            
        elif menu == 4:
            break

    time.sleep(5)  # 실행 완료 후, 지연 5초

if __name__ == "__main__":
    run()