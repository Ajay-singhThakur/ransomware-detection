cat > blockchain/contracts/FileRegistry.sol <<'EOF'
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FileRegistry {
    struct File {
        string ipfsHash;
        address uploader;
        uint256 timestamp;
    }

    File[] public files;

    event FileUploaded(string ipfsHash, address uploader);

    function uploadFile(string memory _ipfsHash) public {
        files.push(File(_ipfsHash, msg.sender, block.timestamp));
        emit FileUploaded(_ipfsHash, msg.sender);
    }

    function getFilesCount() public view returns (uint) {
        return files.length;
    }
}
EOF
