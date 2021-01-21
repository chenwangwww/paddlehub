# 1 "ai.cpp"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "ai.cpp"
# 1 "ai.h" 1
       

class AI
{
    private:
        int mId;
    public:
        AI(int id);
        virtual ~AI();
        int ID() const;
};
# 2 "ai.cpp" 2

AI::AI(int id):mId(id){}

AI::~AI(){}

int AI::ID() const
{
    return mId;
}
