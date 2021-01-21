#include "ai.h"

AI::AI(int id):mId(id){}

AI::~AI(){}

int AI::ID() const
{
    return mId;
}