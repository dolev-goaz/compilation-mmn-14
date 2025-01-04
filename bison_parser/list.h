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

Node* createNode(int data);
List* createList(Node* node);

int isEmpty(List* list);

int equal(List* list);

int sum(List* list);

void append(List* list, int data);

void tail(List* list);

void divide(List* list, int value);

void freeList(List* list);
