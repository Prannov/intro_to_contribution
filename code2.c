#include <stdio.h>
#include <stdlib.h>

// Structure to represent a node in the singly linked list
struct Node {
    int data;
    struct Node* next;
};

// Function to create a new node with the given data
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Function to insert a node at the start of the linked list
void insertAtStart(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Function to insert a node at the end of the linked list
void insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Node* current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
}

// Function to insert a node after a specific node with a given key value
void insertAfterNode(struct Node* prevNode, int data) {
    if (prevNode == NULL) {
        printf("Previous node is NULL. Cannot insert.\n");
        return;
    }
    struct Node* newNode = createNode(data);
    newNode->next = prevNode->next;
    prevNode->next = newNode;
}

// Function to delete the first node in the linked list
void deleteFirstNode(struct Node** head) {
    if (*head == NULL) {
        printf("List is empty. Nothing to delete.\n");
        return;
    }
    struct Node* temp = *head;
    *head = temp->next;
    free(temp);
}

// Function to delete the last node in the linked list
void deleteLastNode(struct Node** head) {
    if (*head == NULL) {
        printf("List is empty. Nothing to delete.\n");
        return;
    }
    if ((*head)->next == NULL) {
        free(*head);
        *head = NULL;
        return;
    }
    struct Node* current = *head;
    while (current->next->next != NULL) {
        current = current->next;
    }
    free(current->next);
    current->next = NULL;
}

// Function to delete a node with a specific key value
void deleteNode(struct Node** head, int key) {
    if (*head == NULL) {
        printf("List is empty. Nothing to delete.\n");
        return;
    }
    if ((*head)->data == key) {
        deleteFirstNode(head);
        return;
    }
    struct Node* current = *head;
    struct Node* prev = NULL;
    while (current != NULL && current->data != key) {
        prev = current;
        current = current->next;
    }
    if (current == NULL) {
        printf("Key not found in the list. Cannot delete.\n");
        return;
    }
    prev->next = current->next;
    free(current);
}

// Function to display the linked list
void displayList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;

    // Insert nodes at the start
    insertAtStart(&head, 3);
    insertAtStart(&head, 2);
    insertAtStart(&head, 1);

    // Display the list
    printf("Linked List after inserting at the start:\n");
    displayList(head);

    // Insert a node at the end
    insertAtEnd(&head, 4);

    // Display the list
    printf("Linked List after inserting at the end:\n");
    displayList(head);

    // Insert a node after a specific node
    insertAfterNode(head->next, 5);

    // Display the list
    printf("Linked List after inserting in between:\n");
    displayList(head);

    // Delete the first node
    deleteFirstNode(&head);

    // Display the list
    printf("Linked List after deleting the first node:\n");
    displayList(head);

    // Delete the last node
    deleteLastNode(&head);

    // Display the list
    printf("Linked List after deleting the last node:\n");
    displayList(head);

    // Delete a specific node
    deleteNode(&head, 3);

    // Display the list
    printf("Linked List after deleting a specific node:\n");
    displayList(head);

    return 0;
}