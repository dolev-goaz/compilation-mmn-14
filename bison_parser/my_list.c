#include "my_list.h"

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

List* createList(int data) {
    List* newList = (List*)malloc(sizeof(List));
    if (!newList) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    Node* node = createNode(data);
    newList->head = node;
    newList->tail = node;

    return newList;
}

int isEmpty(List* list) {
    return (list && list->head)? 0: 1; // ternary to be explicit, wasn't required
}

List* append(List* list, int data) {
    Node* newNode = createNode(data);
    if (isEmpty(list)) {
        list->head = newNode;
        list->tail = newNode;
        return list;
    }
    
    list->tail->next = newNode;
    newNode->prev = list->tail;
    list->tail = list->tail->next;

    return list;
}

// Function to free the linked list
void freeList(List* list) {
    Node* head = list->head;
    Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
    free(list);
}

List* tail(List* list) {
    // if empty
    if (isEmpty(list)) return list;
    // if only 1 node
    if (list->head == list->tail) {
        free(list->head);
        list->head = NULL;
        list->tail = NULL;
        return list;
    }
    // at least 2 nodes
    Node* newTail = list->tail->prev;
    free(list->tail);
    newTail->next = NULL;
    list->tail = newTail;

    return list;
}

// assumes listNode is an element of list
void removeNode(List* list, Node* listNode) {
    if (isEmpty(list)) return;
    if (list->head == list->tail) {
        free(listNode);
        list->head = NULL;
        list->tail = NULL;
        return;
    }

    if (listNode->prev) {
        listNode->prev->next = listNode->next;
    } else {
        list->head = listNode->next;
    }

    if (listNode->next) {
        listNode->next->prev = listNode->prev;
    } else {
        list->tail = listNode->prev;
    }
    free(listNode);

}

List* divide(List* list, int value) {
    if (isEmpty(list)) return list;
    Node* current = list->head;

    while (current) {
        Node* nextNode = current->next;
        if (current->data % value != 0) {
            removeNode(list, current);
        }
        current = nextNode;
    }

    return list;
}

int sum(List* list) {
    if (isEmpty(list)) return 0;
    int sum = 0;
    Node* current = list->head;

    while (current) {
        sum += current->data;
        current = current->next;
    }
    return sum;
}

int equal(List* list) {
    if (isEmpty(list)) return 1;
    
    Node* current = list->head->next;
    
    while (current) {
        if (current->data != list->head->data) {
            return 0;
        }
        current = current->next;
    }
    return 1;
}