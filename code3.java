public class BankAccount {
    private String depositorName;
    private long accountNumber;
    private String accountType;
    private double balanceAmount;
    public void setName(String name) {
        depositorName = name;
    }
    public void setAccountNumber(long accNumber) {
        accountNumber = accNumber;
    }
    public void setAccountType(String accType) {
        accountType = accType;
    }
    public void setBalance(double balance) {
        balanceAmount = balance;
    }
    public void deposit(double amount) {
        if (amount > 0) {
            balanceAmount += amount;
            System.out.println("Deposited $" + amount + " successfully.");
        } else {
            System.out.println("Invalid deposit amount. Please enter a positive amount.");
        }
    }
    public void withdraw(double amount) {
        if (amount > 0) {
            if (balanceAmount >= amount) {
                balanceAmount -= amount;
                System.out.println("Withdrawn $" + amount + " successfully.");
            } else {
                System.out.println("Insufficient balance. Withdrawal failed.");
            }
        } else {
            System.out.println("Invalid withdrawal amount. Please enter a positive amount.");
        }
    }
    public void displayInfo() {
        System.out.println("Account Holder Name: " + depositorName);
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Type: " + accountType);
        System.out.println("Balance: $" + balanceAmount);
    }
    public static void main(String[] args) {
        BankAccount account = new BankAccount();
        account.setName("John Doe");
        account.setAccountNumber(123456789);
        account.setAccountType("Savings");
        account.setBalance(1000.0);
        account.deposit(500.0);
        account.withdraw(200.0);
        account.displayInfo();
    }
}