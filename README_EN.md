# Storage Wars

Storage Wars is an auction-based game and simulation software. The project creates a system where warehouses are sold via auctions, and players, bots (AI), and various products are involved. Players bid in auctions, add items to their inventory, and engage in trading.

## Features

- **Warehouse Management**: Warehouses can be created, filled with random products, and put up for auction.
- **Products**: A wide variety of products with different rarity levels, production dates, and values.
- **Auctions**: A dynamic auction system where both real players and AI can bid.
- **Shops**: Players can sell their items to shops to earn money.
- **Player Management**: Players and AI-based customers can be created and managed.

## Requirements

- Python 3.8 or higher

The project uses Python's built-in modules (e.g., `random`, `time`) and standard libraries. No additional dependencies are required.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/storage-wars.git
    cd storage-wars
    ```

2. Ensure you have Python installed with the required version.

3. Run the project with the following command:
    ```bash
    python Storage-wars.py
    ```

## Usage

1. Upon starting the program, you will see the main menu:
    - Join an auction
    - Check your inventory
    - Sell items

2. In the auction, players take turns to bid. A player can choose to skip bidding or leave the auction.

3. The winner of the auction receives all the items in the warehouse, which are added to their inventory.

4. Players can sell their items to shops to earn money and create more budget for future auctions.

## Code Structure

- **`DepoSavaslari`**: Base class. All other classes are derived from this.
- **`Warehouse`**: Manages warehouses and related operations.
- **`Product`**: Contains products and their properties.
- **`Shop`**: Includes shops and item trading operations.
- **`Auction`**: Manages the auction process and rules.
- **`Customer`, `Player`, `AI`**: Represents players and bots.

## Development

To contribute to the project, follow these steps:

1. Extend the `Product` or `Shop` classes to add new products or shops.
2. Modify the `Auction` class to add new rules or features to the auction process.
3. Improve the AI bidding logic by editing the `AI` class.

## Contribution

Contributions are welcome! Please open an issue to discuss your changes before making them.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to your branch (`git push origin feature/new-feature`).
5. Open a pull request (PR).


## Contact

For questions or suggestions about the project, feel free to contact us:

- **Email**: goooglenudle@gmail.com
- **GitHub**: [Furkan-Demircan](https://github.com/Furkan-Demircan)

---

Have fun and good luck!
