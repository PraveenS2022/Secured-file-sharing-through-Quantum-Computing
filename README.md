**Secured File Sharing Through Quantum Computing**

**Overview**
This project implements a secure file-sharing system that leverages **Advanced Encryption Standard (AES)** and **Quantum Cryptography** to ensure resilience against classical and quantum-based attacks. By integrating **Quantum Key Distribution (QKD)** and **steganography**, the system facilitates secure key exchange and covert data transmission. It utilizes **AWS Cloud Storage** for scalable and remote access while maintaining data integrity, making it suitable for critical industries like finance, healthcare, and defense.

**Output**
![1](https://github.com/user-attachments/assets/f25a8a72-7f7c-4f04-8307-5be7f0473150)
![2](https://github.com/user-attachments/assets/c32e2fe3-57b2-4f36-b0d3-8b0e9d2651d6)
![3](https://github.com/user-attachments/assets/5dc0fb7f-589d-43d1-a9c8-39fd72020f5f)
![4](https://github.com/user-attachments/assets/15a5181f-9e05-4fea-a1d0-9352a1da404d)
![5](https://github.com/user-attachments/assets/753ee364-f68e-45e0-92d4-06305db235c5)



**Features**
- **Quantum Key Distribution (QKD):** Ensures secure key exchange with quantum cryptographic techniques.  
- **Advanced Encryption Standard (AES):** Provides robust encryption for sensitive data.  
- **Steganography:** Embeds encrypted data into images for covert file transmission.  
- **AWS Cloud Integration:** Offers scalable and efficient file storage and access.  
- **Future-Proof Security:** Combines classical and quantum-resistant encryption methods.  
- **Performance Validations:** Rigorous testing for reliability, efficiency, and resilience against quantum threats.  

**Technologies Used**
- **Quantum Computing** (Quantum Key Distribution)  
- **AES Encryption**  
- **Steganography**  
- **AWS Cloud Services**  
- **Python/Other Relevant Programming Languages**  

**Getting Started**

**Prerequisites**
1. Install [Python](https://www.python.org/) (or any language used).  
2. Set up an AWS account for cloud storage services.  
3. (Optional) Quantum Cryptography libraries/frameworks if specific to the project (e.g., Qiskit).  

**Installation**
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/quantum-secure-file-sharing.git
   cd quantum-secure-file-sharing
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Configure AWS credentials for cloud access.  

 **Usage**
1. Run the key generation module for **Quantum Key Distribution (QKD)**:  
   ```bash
   python qkd_key_generation.py
   ```
2. Encrypt the file using AES:  
   ```bash
   python aes_encrypt.py --input <file_path>
   ```
3. Embed the encrypted file into an image using steganography:  
   ```bash
   python steganography_embed.py --image <image_path> --data <encrypted_file>
   ```
4. Upload the steganographed image to AWS Cloud Storage:  
   ```bash
   python upload_to_aws.py --file <file_path>
   ```

**File Sharing Process**
1. The recipient downloads the steganographed image from AWS.  
2. Extract the encrypted data using the steganography extraction module.  
3. Decrypt the file using the AES decryption module and the shared quantum key.  

**Project Architecture**
- **Encryption**: AES + Quantum Cryptographic keys  
- **Data Transmission**: Steganography for covert channels  
- **Cloud Integration**: AWS for secure, scalable storage  

 **Performance Testing**
The system has been validated for:  
- **Encryption and Decryption Time**  
- **Steganographic Embedding and Extraction Speed**  
- **Quantum Resilience**  
- **AWS File Access Latency**  

 **Applications**
- Finance: Secure transactions and sensitive data sharing.  
- Healthcare: Protection of patient records and research data.  
- Defense: Confidential communication and secure file exchanges.  

 **Contributing**
Contributions are welcome! Please follow these steps:  
1. Fork the repository.  
2. Create a new branch for your feature:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Add your message here"
   ```  
4. Push your branch:  
   ```bash
   git push origin feature-name
   ```  
5. Open a pull request.  

## **License**
This project is licensed under the [MIT License](LICENSE).

## **Acknowledgments**
- **Quantum Computing Libraries/Resources** (if applicable).
