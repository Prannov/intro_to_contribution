class AccountCons {
    protected String customerName;
    protected long accountNumber;
    protected String accountType;
    protected double balance;
    public AccountCons(String name, long accNumber, String accType, double initialBalance) {
        customerName = name;
        accountNumber = accNumber;
        accountType = accType;
        balance = initialBalance;
    }
}
class CurrAccount extends AccountCons {
    private double minimumBalance;
    private double penalty;
    public CurrAccount(String name, long accNumber, double initialBalance, double minBalance, double penalty) {
        super(name, accNumber, "Current Account", initialBalance);
        minimumBalance = minBalance;
        this.penalty = penalty;
    }
}
class SavAccount extends AccountCons {
    private double interestRate;
    public SavAccount(String name, long accNumber, double initialBalance, double interestRate) {
        super(name, accNumber, "Savings Account", initialBalance);
        this.interestRate = interestRate;
    }}

public class Main {
    public static void main(String[] args) {
        CurrAccount currentAccount = new CurrAccount("John Doe", 123456789, 2000.0, 1000.0, 50.0);
        SavAccount savingsAccount = new SavAccount("Jane Smith", 987654321, 5000.0, 5.0);
    }
}