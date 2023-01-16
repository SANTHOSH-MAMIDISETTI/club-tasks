int birthdayCakeCandles(vector<int> candles) 
{
    sort(candles.begin(),candles.end(),greater<int>());
    int a = candles.front();
    int count = 0;
    for (auto i : candles)
        {
            if (i>= a) 
            {
                count++;
            }
        }

    return count;
}
