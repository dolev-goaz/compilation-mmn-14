#pragma once

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    struct Node* prev;
    int data;
    struct Node* next;
} Node;

typedef struct List {
    Node* head;
    Node* tail;
} List;

List* createList(int data);

int isEmpty(List* list);

int equal(List* list);

int sum(List* list);

List* append(List* list, int data);

List* tail(List* list);

List* divide(List* list, int value);

void freeList(List* list);
