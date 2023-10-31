#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
    struct Node* next;
};

// EMPTY CIRCULAR LINKED LIST
struct Node* head = NULL;

struct Node* createNode(int data) 
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// INSERT AT START
void insertAtStart(int data) 
{
    struct Node* newNode = createNode(data);

    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        struct Node* current = head;
        while (current->next != head) {
            current = current->next;
        }
        current->next = newNode;
        newNode->next = head;
        head = newNode;
    }
}

// INSERT AT END
void insertAtEnd(int data) 
{
    struct Node* newNode = createNode(data);

    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        struct Node* current = head;
        while (current->next != head) {
            current = current->next;
        }
        current->next = newNode;
        newNode->next = head;
    }
}

// INSERT INBETWEEN
void insertAfterNode(int prevData, int data) 
{
    if (head == NULL) {
        printf("List is empty. Cannot insert.\n");
        return;
    }

    struct Node* current = head;
    do {
        if (current->data == prevData) {
            struct Node* newNode = createNode(data);
            newNode->next = current->next;
            current->next = newNode;
            return;
        }
        current = current->next;
    } while (current != head);

    printf("Node with data %d not found. Cannot insert.\n", prevData);
}

// DELETE AT START
void deleteAtStart() 
{
    if (head == NULL) {
        printf("List is empty. Cannot delete.\n");
        return;
    }

    struct Node* current = head;
    while (current->next != head) {
        current = current->next;
    }

    struct Node* temp = head;
    if (current == head) {
        head = NULL; 
    } else {
        head = head->next;
        current->next = head;
    }
    free(temp);
}

// DELETE LAST NODE
void deleteAtEnd() 
{
    if (head == NULL) {
        printf("List is empty. Cannot delete.\n");
        return;
    }

    struct Node* current = head;
    struct Node* previous = NULL;

    do {
        previous = current;
        current = current->next;
    } while (current->next != head);

    if (current == head) {
        head = NULL; 
    } else {
        previous->next = head;
    }
    free(current);
}

// DELETE INBETWEEN
void deleteNode(int data) 
{
    if (head == NULL) {
        printf("List is empty. Cannot delete.\n");
        return;
    }

    struct Node* current = head;
    struct Node* previous = NULL;

    do {
        if (current->data == data) {
            if (current == head) {
                deleteAtStart();
            } else {
                previous->next = current->next;
                free(current);
            }
            return;
        }
        previous = current;
        current = current->next;
    } while (current != head);

    printf("Node with data %d not found. Cannot delete.\n", data);
}

//DISPLAY
void displayList() 
{
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    struct Node* current = head;

    do {
        printf("%d -> ", current->data);
        current = current->next;
    } while (current != head);

    printf("\n");
}

int main() 
{
    int choice, data, prevData;

    while (1) {
        printf("\nCircular Linked List Operations:\n");
        printf("1. Insert at the start\n");
        printf("2. Insert at the end\n");
        printf("3. Insert after a specific node\n");
        printf("4. Delete at the start\n");
        printf("5. Delete at the end\n");
        printf("6. Delete a specific node\n");
        printf("7. Display the list\n");
        printf("8. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data to insert at the start: ");
                scanf("%d", &data);
                insertAtStart(data);
                break;

            case 2:
                printf("Enter data to insert at the end: ");
                scanf("%d", &data);
                insertAtEnd(data);
                break;

            case 3:
                printf("Enter data to insert: ");
                scanf("%d", &data);
                printf("Enter data of the node after which to insert: ");
                scanf("%d", &prevData);
                insertAfterNode(prevData, data);
                break;

            case 4:
                deleteAtStart();
                break;

            case 5:
                deleteAtEnd();
                break;

            case 6:
                printf("Enter data to delete: ");
                scanf("%d", &data);
                deleteNode(data);
                break;

            case 7:
                printf("Circular Linked List:\n");
                displayList();
                break;

            case 8:
                exit(0);

            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}