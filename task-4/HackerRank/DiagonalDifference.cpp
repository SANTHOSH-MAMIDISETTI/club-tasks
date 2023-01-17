int diagonalDifference(vector<vector<int>> vect) {
    
    int p,s,i,j; 
    p = s =0;
    
    for (int i = 0; i < vect.size(); i++)
    {
        for (int j = i; j <=i; j++)
        {
            p+=vect[i][j];
        }    
        cout << endl;
    }

    for (int i = 0; i < vect.size(); i++)
    {
        for (int j = vect[i].size()-1-i; j <=vect[i].size()-1-i; j++)
        {
            s+=vect[i][j];
        }    
    }
    
    return abs(p-s);
}