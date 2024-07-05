/*
	Name: randConcept
	Author: KingMak
	Date: 22/07/15 00:18
	Description: an attemp to get a random number from the given range
*/

#include <cmath>
#include <ctime>
#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	int i = 0;
	int errorCount = 0;
	double max = 346.5; // range max
	double min = 313.5; // range min
	double magicNumber = 0.5; // 0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9 are erroneous 1.0 gives only x.5 outputs
	double formula;

	// seed
	srand(time(NULL));

	for (; i < 100000; i++)
	{
		formula = min + fmod(rand(), ((max - min) + magicNumber)); // fmod is modulus with double/float, used from cmath

		if ((formula > max) || (formula < min))
		{
			cout << "PROBLEM: output = " << formula << endl;
			errorCount++;
		}

		cout << formula << endl; // <- uncomment if want to see output of random numbers
	}

	if (errorCount > 0)
	{
		cout << "number of incorrect outputs = " << errorCount << endl;
	}

	cout << "done" << endl;
	return 0;
}
