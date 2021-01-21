#pragma once

class AI
{
    private:
        int mId;
    public:
        AI(int id);
        virtual ~AI();
        int ID() const;
};