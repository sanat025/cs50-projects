#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");
    int letters = 0;
    int words = 0;
    int sentences = 0;
    bool in_word = false;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        char c = text[i];
        if (isalpha(c))
        {
            letters++;
            if (!in_word)
            {
                in_word = true;
                words++;
            }
        }
        else
        {
            if (isspace(c))
            {
                in_word = false;
            }
            if (c == '.' || c == '!' || c == '?')
            {
                sentences++;
            }
        }
    }

    if (words == 0)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    float L = (letters * 100.0f) / words;
    float S = (sentences * 100.0f) / words;
    int index = (int) round(0.0588f * L - 0.296f * S - 15.8f);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
    return 0;
}
