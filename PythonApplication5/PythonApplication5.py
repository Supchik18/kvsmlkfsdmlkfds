import json
import time
import random
inventar=0
def save():
    name_saved = name
    inventar_saved = inventar
    save = {
        "Name":name_saved,
        "inventar":inventar_saved
    }
    with open('save.json','w+') as file:
        json.dump(save,file)
    print ("������ ���������")

 def load():
            with open('save.json','r')as file:
                save = json.load(file)
            name_saved  = save['name']
            inventar_saved = save['inventar']
            print("������ ���������")


def cdoh ():
    print ("�� ������..")
    exit()
def sa():
    print ("�� ������ ���������� ������ � ������� ������ ����������� ���� � ����... �� ������� ������ ��������� ���������� �����")
    time.sleep (1)
    print ("�������� ��� ������ ������: 1 ������ ��� ������. 2 ������ ����� �� ���� � ����� ������, ����� ��� ��������� ��� ������")
    sa2=str(input("������� �����: "))
    if sa2=="1":
        print ("�� ������ ����... ����� ��������� ������, ��� ��� ���� �� �������� �������� ��� � ���, ��� ��� ����������� � ����� �������")
        time.sleep (1)
        cdoh()
    else:
        print ("������ �� ������ ������� �����... ��� �������, ��� ���� ���������, �� ��� �� ��� � ��� ������.")
        time.sleep(1)
        print ("� ����� ��� ������������ �� ��������� � ���� � ����� ���.")
        time.sleep(1)
        print ("�������� ��� ��������: 1. �������. 2. ����������� ������������")
        t=int(input())
        if t==1:
            print ("�� �������!")
        if t==2:
            cdoh()
def ga():
    print ("�� ���������� �������, ��� ����� ������ ���, ��� ��� ���� ����� �� ������ �������, �� ��� �� ���������.")
    time.sleep (1)
    print ("������ �������: � ����� ���� �������� ��� �������� � ��� ����.� ���� ������� �������. ���������, ��� ������.")
    zag1=str(input("������� �����: "))
    if zag1=="����� � �����":
        print ("�� �������!")
    else:
        print ("\"�� ������! ����� ��� ���!\"")
        time.sleep (1)
        print ("����� ������� � ��� ��� ����� ����� ����.")
        print ("������� �����")
        wq=str(input("������� �����: "))
        if wq=="����������":
            print ("�� �������!")
        else:
            cdoh()
def fa():
    print ("�� �������� �����... �� ������ � ���������?")
    time.sleep(1)
    print ("1. �� 2. ���")
    time.sleep(1)
    x=int(input())
    if x==1:
        print ("����� ��������� ����� � ��������� ���")
        cdoh()
    else:
        print ("�� ������ �� �������)")
def game():
    print("�� ������������ � ����... �� �� ������ ��� ����������, ������� ����� ���� ��")
    x=random.randint(1,3)
    if x==1:
        sa()
    if x==2:
        ga()
    if x==3:
        fa()
print ("������� ���")
name = input()
save()
game()
f=f"� ���� �� ���� ������"
print ("�� ����� ��� ���� ������ ������...")
time.sleep(1)
print ("� ������ �� ������ ������ �������� ���, ������ �� ����� �������, ��� �� ������ ��� ���")
time.sleep (1)
print ("�� ��������� �������, ��� � ����")
time.sleep(1)
print ("� ������ �������� �������� � ����, ������ ��� ������")
time.sleep(1)
print ("���� �� ������?")
time.sleep(1)
print ("1. �� �����, � ���� ����. 2. � ���������, ����� ����� ���� ��� �� ������� ��� ����� �������. 3. � �������, � �����, ���� �� �������.")
time.sleep(1)
o=int(input())
if o==1:
    print ("�� ������� �� �����... ���, ����� ����������... �� ������ ����� �...")
    time.sleep(1)
    print ("� ���� �������, ������� �� ������... �� ������ ����������� � ������ ����� ��� �� ���� ����, �� ����� �� ������� � �������.")
    time.sleep(1)
    inventar=str("���� �����!")
if o==2:
    print ("�� ��������� � ���������, ��� � ������ ���� ���������� ������� ���������...")
    time.sleep (1)
    print ("����� �� ����� �� �������� ����� ��������, ������� ����, �� ������ ����� �, �� ������� � �������.")
    time.sleep (1)
    inventar=str("��������, ������� ����!")
if o==3:
    print ("�� �������� ����� � �������, ������ ������ ��� �� ��������")
    time.sleep (1)
load()
wa = ["������� ��������", "������ ��������"]
print ("�� �������� �� �������... ���� ���� �����, � ����� ����������� ����� �����")
time.sleep (1)
print ("� ��� �� ������������... ������ �� �� ���������� ��� ��� ����� �������... ")
time.sleep (1)
print ("��� ��������� �����...")
time.sleep (1)
print ("����� ����� ������� �� ���, � � ����� �� ����� ������ ����...")
time.sleep (1)
print ("� ��� � ����� ������ ������ ����������... ������� ��� �� ��� ��� �� �����, ��� �� ���")
time.sleep (1)
print ("��� �� ��������? 1. ���������� ��� �������. 2. ���������� � ����. 3 ��������� ��� ����� ������ ")
time.sleep (1)
c=int(input())
if c==1:
    print ("�� ��������� ��� �������.")
    time.sleep (1)
    print ("�� ������� ��� ������ ���� ������, ���� �� �� ��������� �� �����.")
    time.sleep (1)
    print ("���� ������� ��� �����, �� ���������� ���..")
    time.sleep (1)
    print ("�� ������ ��������� ����� ����� ���?")
    time.sleep (1)
    print ("�� �� ��������� ������, ��� ���������... ��� ���������� �� ����")
    time.sleep (1)
    print (wa [1])
    cdoh()
if c==2:
    print ("�� ������������ � ����...")
    time.sleep (1)
    print ("����� ��� ������ ��� � ������ ���� ������� ����� ��� � ����...")
    time.sleep (1)
    print ("�� ������� ��� �� ������, �� ����������, ��� ��� ��� �������� ������� ����")
    time.sleep (1)
    print ("������ ���� �� ������ ��� ��� ��������� ��� ��... ��� ���")
    time.sleep (1)
    print (wa [1])
    cdoh ()
if c==3:
    print ("�� ������ ��� ����� �������� �����������...")
    time.sleep (1)
    print ("������ ������������... �����?")
    time.sleep (1)
    print ("��� ������� �� ���, ������� ������ ��� �� ��� �������..")
    time.sleep (1)
    print ("\" ��� �� ��� �������?! � ����... �� �������, ��� ������ ���� �������, ��� �� ����!... ������ �����, ��� ���� �����?\"")
    time.sleep (1)
    print ("������� ��� �����:")
    time.sleep (1)
    name2 = input()
    time.sleep (1)
    print("��� �� �����������, ��", name2, " ��������� �������������, ������� ������ ��� ����������...")
    time.sleep (1)
    print("��� ������ ������ ���������, ����� ����� �� �����, ��� �� ���� � ��������� ������� ���� �����������...")
    time.sleep (1)
    print("����� ��� ���� ����� � ��� ��� ����� ��������")
    time.sleep (1)
    print("�� ����� � ������... ����� �������, ��� ��� ����� �����, ���� ������ ���� ��� ����")
    time.sleep (1)
    print("��� �� ��������? 1. �������� �� ���� ������� ���������� ������� ���������. ����� ���� ���������� �. 2. ����� ������ � ������� �. 3. ��������� ������ ������ ��� �� �����")
    time.sleep (1)
    t=int(input())
    print("�� ����� � ���������� ������... ��������, �� ����� �� ������������� � ����� ����.")
    time.sleep (1)
    print("�� ��� ������ �����...")
    time.sleep (1)
    print("������ �������, ��� ����� �������� ��������� � ����� �������.")
    time.sleep (1)
    print("��� ��� �������������... ���� ������ �������")
    time.sleep (1)
    if t==1:
        print("�� ����������� ��� �������� ��������� �� ����...")
        time.sleep (1)
        print("� ����� � ���� ������ ���� �����������...")
        time.sleep (1)
        print("�� � ����� �� ������ �������...")
        time.sleep (1)
        cdoh()
    if t==2:
        print("������ ����� ��������� ������...")
        time.sleep (1)
        print("�� ������ � ������� ������ �������")
        time.sleep (1)
        print (wa[0])
    if t==3:
        print("�� ��������� ������...")
        time.sleep (1)
        print("������ ��� ��������...")
        time.sleep (1)
        print("��������� ��� ����� ������� ����� ������ ������� ������...")
        time.sleep (1)
        print("�� �������������� ��������...")
        time.sleep (1)
        print("��� ����� ������� ���� ����� ��� ������")
        time.sleep (1)
        print("� ����� ��������� ������ ���")
        time.sleep (1)
        print("��� ��� ���� ���� ����� ����� ����� �������")
        time.sleep (1)
        print("�� ��� ���� �� �� �����")
        time.sleep (1)
        print("����� �� ������� ������� ���, ������ ������ ��������..������ ����:")
        time.sleep (1)
        print (f)
        print("��� ��������� � ������.")
        time.sleep (1)
        cdoh ()
        def save_csv():
            name_saved = name
            inventar_saved = inventar
            save = [
            [date.today(), name_saved, inventar_saved]
            ]
            with open("save.csv",'w+',newline='') as file:
            writer = csv.writer(file)
        save_csv()
        print ("�������� ������")
        with open ('nested.json', 'r') as file:
            data = json.load (file)
        del data ["address"]["zip"]
        with open ('nested.json', 'w' ) as file:
            json.dump (data, file, indent =4)








