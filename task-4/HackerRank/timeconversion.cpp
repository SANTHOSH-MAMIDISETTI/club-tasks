string timeConversion(string s) 
{   
    for (int i = 0;i<10; i++) 
    {
        if (s [8] == 'A') 
        {   if (s.at(0)=='1'&& s.at(1)=='2')
                {
                    s[0] = s[1] = '0';
                    string rr = s.substr(0, 8);
                    return rr;
                }
            else
            {
            string rr = s.substr(0, 8);
            return rr;
            }
            
        }
        else if(s[8] == 'P')
        {   
            if (s.at(0)=='1'&& s.at(1)=='2')
                {   
                    s[0] = '1';
                    s[1] = '2';
                    string rr = s.substr(0, 8);
                    return rr;
                }
            else
            {
                string r = s.substr(0, 2);
                string end = s.substr(2, 6);
                int num = std::stoi(r);
                int final_n = num+12;
                std::string num_str = std::to_string(final_n);
                string final_str = num_str+end;
                return final_str;
            }   
        }
    }
    return s;
}
