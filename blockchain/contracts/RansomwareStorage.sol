// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "hardhat/console.sol";

contract RansomwareStorage {
    address public owner;

    struct FileRecord {
        string fileName;
        string fileHash; // SHA-256 hash of the file content
        string ipfsCid; // IPFS content identifier
        string detectionResult;
        uint256 timestamp;
    }

    FileRecord[] public fileRecords;

    event FileRecordAdded(
        uint256 indexed id,
        string fileName,
        string fileHash,
        string ipfsCid,
        string detectionResult,
        uint256 timestamp
    );

    constructor() {
        owner = msg.sender;
    }

    function addFileRecord(
        string memory _fileName,
        string memory _fileHash,
        string memory _ipfsCid,
        string memory _detectionResult
    ) public {
        // In a real-world scenario, you might want to restrict who can call this
        // require(msg.sender == owner, "Only owner can add records");

        uint256 newId = fileRecords.length;
        fileRecords.push(
            FileRecord({
                fileName: _fileName,
                fileHash: _fileHash,
                ipfsCid: _ipfsCid,
                detectionResult: _detectionResult,
                timestamp: block.timestamp
            })
        );

        emit FileRecordAdded(
            newId,
            _fileName,
            _fileHash,
            _ipfsCid,
            _detectionResult,
            block.timestamp
        );
        console.log("File record added for %s", _fileName);
    }

    function getFileRecordsCount() public view returns (uint256) {
        return fileRecords.length;
    }
}