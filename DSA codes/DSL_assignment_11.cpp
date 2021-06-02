#include<iostream>
using namespace std;
#define max 5
class Queue
{
private:
    int queue[max];
    int front,rear;
public:
    Queue();
    bool isFull();
    bool isEmpty();
    void addJob(int j);
    void delJob();
    void display();
};

Queue::Queue()
{
    front=-1;
    rear=-1;
}
bool Queue::isFull(){
    if (rear==max-1)
    {
        return 1;
    }
    else{
        return false;
    }
}
bool Queue::isEmpty(){
    if (rear==front)
    {
        return 1;
    }
    else{
        return false;
    }
}
void Queue::addJob(int j){
    if (rear==max-1)
    {
        cout<<"Queue overflow "<<endl;
    }
    else if(rear==-1 && front==-1){
        front=0;
        queue[++rear]=j;
        cout<<j<<" inserted successfully "<<endl;
    }
    else{
        queue[++rear]=j;
        cout<<j<<" inserted successfully "<<endl;
    }
}
void Queue::delJob(){
    if (rear==-1 && front==-1)
    {
        cout<<"Queue underflow "<<endl;
    }
    else if(rear == front){
        cout<<queue[front]<<" deleted successfully "<<endl;
        rear =-1;
        front=-1;
    }
    else{
        cout<<queue[front]<<" deleted successfully "<<endl;
        front++;
    }
}
void Queue::display(){
    cout<<"queue is : ";
    for (int i = front; i < rear+1; i++)
    {
        cout<<queue[i]<<"  ";
    }
    cout<<endl;
}
int main(){
int x,choice;
Queue q;
while (true)
{
    cout<<"\n1.Insert\n2.Delete\n3.Display\nEnter choice : ";
    cin>>choice;
    if (choice==0)
    {
        break;
    }
    switch (choice)
    {
    case 1:
        cout<<"enter job code : ";
        cin>>x;
        q.addJob(x);
        break;
    case 2:
        q.delJob();
        break;

    case 3:
        q.display();
        break;
    default:
        break;
    }
}

return 0;
}