vector<int> compareTriplets(vector<int> a, vector<int> b) 
{
    vector<int> result(2);
for(int i=0; i<3; i++)
{ 
    if(a[i]>b[i])
        result[0] = result[0]+1; 
    else if( a[i]<b[i])
        result[1] = result[1]+1;
}
return result;
}