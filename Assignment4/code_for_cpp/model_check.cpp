#include "logic.cpp"

int main() {
    shared_ptr<Sentence> A = make_shared<Symbol>("A");
    shared_ptr<Sentence> B = make_shared<Symbol>("B");
    shared_ptr<Sentence> C = make_shared<Symbol>("C");

    shared_ptr<Sentence> knowledge = make_shared<And>(
        initializer_list<shared_ptr<Sentence>>{
            make_shared<Implication>(A, B),
            make_shared<Implication>(B, C),
            A
        });

    shared_ptr<Sentence> query = C;

    cout << "Knowledge Base: " << knowledge->formula() << endl;
    cout << "Query: " << query->formula() << endl;

    if (model_check(*knowledge, *query)) {
        cout << "Knowledge entails the query." << endl;
    } else {
        cout << "Knowledge does not entail the query." << endl;
    }

    return 0;
}
