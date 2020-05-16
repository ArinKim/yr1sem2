using System;
using System.Threading;

namespace Life
{
    /// <summary>
    /// Contains methods used to run Conway's Game of Life
    /// </summary>
    /// <author>
    /// Arin Kim : n9908544
    /// </author>
    public static class Conway
    {
        /// <summary>
        /// A random number generator used during creation
        /// </summary>
        private static Random rng = new Random();
        /// <summary>
        /// Static value of alive and death used for boolean var
        /// </summary>
        private static bool alive = true;
        private static bool death = false;
        /// <summary>
        /// Enum of life about death and alive used for making grid
        /// </summary>
        enum Life { Death, Alive };
        /// <summary>
        /// Provid the speed of update time
        /// </summary>
        const int UPDATE_TIME = 150;
        /// <summary>
        /// Provid the maxumum running time used to stop the loop
        /// </summary>
        const int Max_running = 300;


        /// <summary>
        /// Runs the game of life according to its rules and continuously refreshes the result
        /// </summary>
        public static void Main()
        {
            // Initialize of integer of rows and columns used for user input
            int rows;
            int cols;

            // Assign the value of running times used for ending
            int running = 0;
            
            // Greeting user to enter their own size of grid
            Console.WriteLine("Welcom to the game of life!");

            // Asking about lenghth of row to player
            Console.WriteLine("How many rows of field do you want to play?: ");
            
            int.TryParse(Console.ReadLine(), out rows); //Get lenghth of row into integer

            // Asking about lenghth of column to player
            Console.WriteLine("How many columns of field do you want to play?: ");
            
            int.TryParse(Console.ReadLine(), out cols); //Get lenghth of column into integer

            // Make the first generation
            bool[,] grid = MakeGrid(rows, cols);

            // Repeat to update and draw the grid until fix the life
            do
            {
                Console.Clear(); // Clear the screen
                DrawGrid(grid); // Draw standard grid
                grid = UpdateGrid(grid); // Update next generation into standard grid

                // Make the game slower
                System.Threading.Thread.Sleep(UPDATE_TIME);

            } while (running ++ < Max_running); // Stop to play the game when running time is same with maximum running time.

            // Comment about end of this game
            Console.WriteLine("This is end of game!");
            Console.ReadLine();

        }

        /// <summary>
        /// Returns a new grid for Conway's Game of life using the given dimensions.
        /// Each cell has a 50% chance of initially being alive.
        /// </summary>
        /// <param name="rows">The desired number of rows</param>
        /// <param name="cols">The desired number of columns</param>
        /// <returns></returns>
        public static bool[,] MakeGrid(int rows, int cols)
        {
            bool[,] grid = new bool[rows, cols]; // Initialize empty array
            

            for (int row = 0; row < grid.GetLength(0); row++)
            {
                for (int column = 0; column < grid.GetLength(1); column++)
                {
                    // Get the random numbers between 0 to 1 as
                    // each cell has a 50% chance of initially being alive.
                    int num = rng.Next(minValue: 0, maxValue: 1 + 1);

                    
                    // If random number is 1
                    if (num == (int)Life.Alive)
                    {
                        grid[row, column] = alive; // Get the value of alive
                    }
                    // If random number is 0
                    else if (num == (int)Life.Death)
                    {
                        grid[row, column] = death; // Get the value of death
                    }
                }
            }

            return grid;

        }

        /// <summary>
        /// Writes the given game grid to standard output
        /// </summary>
        /// <param name="grid">The grid to draw to standard output</param>
        public static void DrawGrid(bool[,] grid)
        {
            // Draw the given game grid to standard output by using '.' and '#'
            for (int row = 0; row < grid.GetLength(0); row++)
            {
                for (int column = 0; column < grid.GetLength(1); column++)
                {
                    if (grid[row, column] == alive) // if it is alive
                    {
                        Console.Write("#");
                    }
                    else if (grid[row, column] == death) // if it is death
                    {
                        Console.Write(".");
                    }

                }

                // Change the line because we need to draw a 'grid'
                Console.WriteLine();
            }
            
        }

        /// <summary>
        /// Returns the number of living neighbours adjacent to a given cell position
        /// </summary>
        /// <param name="grid">The game grid</param>
        /// <param name="row">The cell's row</param>
        /// <param name="col">The cell's column</param>
        /// <returns>The number of adjacent living neighbours</returns>
        public static int CountNeighbours(bool[,] grid, int row, int col)
        {
            // Initialize the valude of count of living cell
            int liveCount = 0;

            // Check the neighbours with the value of row and col
            for (int rowNeighbours = -1; rowNeighbours < 2; rowNeighbours++)
            {
                for (int colNeighbours = -1; colNeighbours < 2; colNeighbours++)
                {
                    // If the neighbours are located out of grid or
                    // if the row and col is on same location
                    if ((row + rowNeighbours < 0 || col + colNeighbours < 0) ||
                        (rowNeighbours == 0 && colNeighbours == 0))
                    {
                        continue;
                    }

                    // If neibours are located under the length of grid
                    if (row + rowNeighbours < grid.GetLength(0) &&
                        col + colNeighbours < grid.GetLength(1))
                    {
                        // If the grid is alive
                        if (grid[row + rowNeighbours, col + colNeighbours] == alive)
                        {
                            liveCount++;
                        }
                    }
                }
            }
            
            return liveCount;
        }

        /// <summary>
        /// Returns an updated grid after progressing the rules of the Game of Life.
        /// </summary>
        /// <param name="grid">The original grid from which the new grid is derived</param>
        /// <returns>A new grid which has been updated by one time-step</returns>
        public static bool[,] UpdateGrid(bool[,] grid)
        {
            // Count alive cells from specific position
            // and update grid into next generation grid
            int aliveCount;
            bool[,] future = new bool[grid.GetLength(0), grid.GetLength(1)];

            // Check evey neighbours
            for (int row = 0; row < grid.GetLength(0); row++)
            {
                for (int column = 0; column < grid.GetLength(1); column++)
                {
                    // Assign the value of alive count for each cells
                    aliveCount = CountNeighbours(grid, row, column);

                    // Any live cell with fewer than two live neighbors dies, as if by underpopulation.
                    if (grid[row, column] == alive && aliveCount < 2)
                    {
                        future[row, column] = death;
                    }
                    // Any live cell with two or three live neighbors lives on to the next generation.
                    else if (grid[row, column] == alive && aliveCount > 3)
                    {
                        future[row, column] = death;
                    }
                    // Any live cell with more than three live neighbors dies, as if by overpopulation.
                    else if (grid[row, column] == alive && (aliveCount == 2 || aliveCount == 3))
                    {
                        future[row, column] = alive;
                    }
                    // Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    else if (grid[row, column] == death && aliveCount == 3)
                    {
                        future[row, column] = alive;
                    }

                }
            }

            return future;
        }
    }
}
