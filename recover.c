#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc !=2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    uint8_t buffer[BLOCK_SIZE];
    FILE *output = NULL;

    int file_count =0;
    bool found_jpeg = false;

    while (fread(buffer, BLOCK_SIZE, 1, input) == 1)
    {
        bool is_jpeg_header =
            buffer[0] == 0xff &&
            buffer [1] == 0xd8 &&
            buffer [2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0;

        if (is_jpeg_header)
        {
            if (output != NULL)
            {
                fclose(output);
            }

            char filename[8];
            sprintf(filename, "%03i.jpg", file_count);
            output = fopen(filename, "wb");
            if (output == NULL)
            {
                fclose(input);
                return 1;
            }

            file_count++;
        }

        if (output != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, output);
        }
    }


}
