class node:
    def __init__(self,num):
        self.num = num
        self.back = None
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self,num):
        new = node(num)

        if self.head == None:
            self.head = new
        else:
            last = self.head
            while (1):
                if last.next == None:
                    break
                else:
                    last = last.next
            last.next = new
            new.back = last

    def start(self,num):
        new = node(num)

        pointer = self.head
        new.next = pointer
        pointer.back = new
        self.head = new

    def delete(self,num):
        pointer = self.head
        while(1):
            if num == pointer.num:
                break
            else:
                pointer = pointer.next

        next = pointer.next
        back = pointer.back

        back.next = pointer.next
        next.back = pointer.back
        pointer.next = None

main = linkedlist()
main.push(44)
main.push(36)
main.push(90)
main.push(10)
main.push(60)
main.push(99)

main.start(104)

main.delete(10)
