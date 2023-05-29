
#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;

int f;

struct node{
    int val;
    struct node *left;
    struct node *right;
};

struct node *newNode(int val) {
  struct node *temp = (struct node *)malloc(sizeof(struct node));
  temp->val = val;
  temp->left = temp->right = NULL;
  return temp;
}

struct node *insert(struct node *node, int val) {

  if (node == NULL) return newNode(val);

  if(val == node->val)
  {
      f=1;
      return node;
  }
  else if (val < node->val)
  {
     f=0;
     node->left = insert(node->left, val);
  }

  else
    {
        f=0;
        node->right = insert(node->right, val);
    }
  return node;
}

bool search(struct node *node, int val) {

  if (node == NULL)
  {
      return false;
  }
  if(val == node->val)
  {
      return true;
  }
  else if (val < node->val)
  {

      search(node->left, val);
  }

  else
  {
      search(node->right, val);
  }
}

void inorder(struct node *root) {

  if (root != NULL) {

    inorder(root->left);
    printf("%d -> ",root->val);
    inorder(root->right);
  }
}


int main(void){

    clock_t start, end;
    double execution_time;

    int number;
    struct node *root = NULL;

    start = clock();

    for (int i = 0; i < 1000; i++)
    {
            number=rand();
            root=insert(root, number);
            while(f==1)
            {
                number=rand();
                root=insert(root, number);
            }
    }

    end = clock();
    execution_time = ((double)(end - start))/CLOCKS_PER_SEC;

    printf("Inorder traversal: \n");
    inorder(root);

    printf("\n");

    printf("\n");
    printf("Time taken to insert in seconds : %f", execution_time);
    printf("\n");

    start = clock();
    for (int i = 0; i < 1000; i++)
    {
            number=rand();
            search(root, number);
    }
    end = clock();
    execution_time = ((double)(end - start))/CLOCKS_PER_SEC;

    printf("\n");
    printf("Time taken to search in seconds : %f", execution_time);
    printf("\n");
    return 0;
}
