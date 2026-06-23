#include <iostream>
#include <sstream>
#include <string>
using namespace std;


class Node{
    public:
        int data; // 4 byte
        Node* next; // 8 byte

    // total = 12 byte
};



void add_node(Node* head, int value){
    Node* new_node = new Node();

    new_node->data = value;
    new_node->next = nullptr;

    if(head == nullptr){
        head = new_node;
        return;
    }

    Node* walker_node = head;

    while(walker_node->next != nullptr){
        walker_node = walker_node->next;
    }

    walker_node->next = new_node;
    

    return;
}

void delete_list(Node*& head){
    Node* walker_node = head;
    Node* curr = nullptr;

    while(walker_node){
        curr = walker_node->next;
        delete walker_node;
        walker_node = curr;
    }

    head = nullptr;
}


void print_list(Node* head){
    Node* walker_node = head;

    // 1 2  
    while(walker_node != nullptr){
        cout << walker_node->data << "->";
        walker_node = walker_node->next;
    }
    cout << "-1" << endl;
}



int main(){
    Node* head = new Node();

    head->data = 1;
    head->next = nullptr;

    Node* sec_node = new Node();

    sec_node->data = 2;
    sec_node->next = nullptr;

    head->next = sec_node;


    Node* third_node = new Node();

    third_node->data = 3;
    third_node->next = nullptr;

    head->next->next = third_node;



    cout << "Nodes value: ";
    cout << head->data << " ";

    cout << head->next->data << " ";
    cout << head->next->next->data << endl;


    string input; // 1 2 3 4 5 6 
    cout << "Input: ";
    getline(cin, input);



    istringstream ss(input); // split space 1,2,3,4,5,6

    int num;
    while(ss >> num){
        add_node(head, num);
    }



    print_list(head);
    delete_list(head);
    print_list(head);

    return 0;
}