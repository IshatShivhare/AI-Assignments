#include <bits/stdc++.h>
using namespace std;

class Sentence {
public:
    virtual bool evaluate(const unordered_map<string, bool>& model) const = 0;
    virtual string formula() const = 0;
    virtual unordered_set<string> symbols() const = 0;
    virtual ~Sentence() = default;
};

class Symbol : public Sentence {
public:
    string name;
    
    Symbol(string name) : name(name) {}

    bool evaluate(const unordered_map<string, bool>& model) const override {
        if (model.count(name)) return model.at(name);
        throw runtime_error("Variable not found in model: " + name);
    }

    string formula() const override {
        return name;
    }

    unordered_set<string> symbols() const override {
        return {name};
    }
};

class Not : public Sentence {
public:
    shared_ptr<Sentence> operand;

    Not(shared_ptr<Sentence> operand) : operand(operand) {}

    bool evaluate(const unordered_map<string, bool>& model) const override {
        return !operand->evaluate(model);
    }

    string formula() const override {
        return "¬" + operand->formula();
    }

    unordered_set<string> symbols() const override {
        return operand->symbols();
    }
};

class And : public Sentence {
public:
    vector<shared_ptr<Sentence>> conjuncts;

    And(initializer_list<shared_ptr<Sentence>> conjuncts) : conjuncts(conjuncts) {}

    bool evaluate(const unordered_map<string, bool>& model) const override {
        return all_of(conjuncts.begin(), conjuncts.end(), [&](auto& c) { return c->evaluate(model); });
    }

    string formula() const override {
        string res;
        for (size_t i = 0; i < conjuncts.size(); ++i) {
            if (i > 0) res += " ∧ ";
            res += conjuncts[i]->formula();
        }
        return res;
    }

    unordered_set<string> symbols() const override {
        unordered_set<string> result;
        for (const auto& conjunct : conjuncts) {
            auto s = conjunct->symbols();
            result.insert(s.begin(), s.end());
        }
        return result;
    }
};

class Or : public Sentence {
public:
    vector<shared_ptr<Sentence>> disjuncts;

    Or(initializer_list<shared_ptr<Sentence>> disjuncts) : disjuncts(disjuncts) {}

    bool evaluate(const unordered_map<string, bool>& model) const override {
        return any_of(disjuncts.begin(), disjuncts.end(), [&](auto& d) { return d->evaluate(model); });
    }

    string formula() const override {
        string res;
        for (size_t i = 0; i < disjuncts.size(); ++i) {
            if (i > 0) res += " ∨ ";
            res += disjuncts[i]->formula();
        }
        return res;
    }

    unordered_set<string> symbols() const override {
        unordered_set<string> result;
        for (const auto& disjunct : disjuncts) {
            auto s = disjunct->symbols();
            result.insert(s.begin(), s.end());
        }
        return result;
    }
};

class Implication : public Sentence {
public:
    shared_ptr<Sentence> antecedent, consequent;

    Implication(shared_ptr<Sentence> a, shared_ptr<Sentence> c) : antecedent(a), consequent(c) {}

    bool evaluate(const unordered_map<string, bool>& model) const override {
        return !antecedent->evaluate(model) || consequent->evaluate(model);
    }

    string formula() const override {
        return antecedent->formula() + " => " + consequent->formula();
    }

    unordered_set<string> symbols() const override {
        auto s = antecedent->symbols();
        auto r = consequent->symbols();
        s.insert(r.begin(), r.end());
        return s;
    }
};

class Biconditional : public Sentence {
public:
    shared_ptr<Sentence> left, right;

    Biconditional(shared_ptr<Sentence> l, shared_ptr<Sentence> r) : left(l), right(r) {}

    bool evaluate(const unordered_map<string, bool>& model) const override {
        return left->evaluate(model) == right->evaluate(model);
    }

    string formula() const override {
        return left->formula() + " <=> " + right->formula();
    }

    unordered_set<string> symbols() const override {
        auto s = left->symbols();
        auto r = right->symbols();
        s.insert(r.begin(), r.end());
        return s;
    }
};

bool check_all(const Sentence& knowledge, const Sentence& query, unordered_set<string> symbols, unordered_map<string, bool> model) {
    if (symbols.empty()) {
        return !knowledge.evaluate(model) || query.evaluate(model);
    }

    string p = *symbols.begin();
    symbols.erase(p);

    auto model_true = model;
    model_true[p] = true;

    auto model_false = model;
    model_false[p] = false;

    return check_all(knowledge, query, symbols, model_true) && check_all(knowledge, query, symbols, model_false);
}

bool model_check(const Sentence& knowledge, const Sentence& query) {
    unordered_set<string> symbols = knowledge.symbols();
    unordered_set<string> query_symbols = query.symbols();
    symbols.insert(query_symbols.begin(), query_symbols.end());

    return check_all(knowledge, query, symbols, {});
}