// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RansomwareStorage {
    struct FileEvent {
        string filename;
        string ipfsHash;
        string status;
        uint256 timestamp;
    }

    FileEvent[] public events;

    function storeFileEvent(string memory filename, string memory ipfsHash, string memory status) public {
        events.push(FileEvent(filename, ipfsHash, status, block.timestamp));
    }

    function getEventsCount() public view returns (uint256) {
        return events.length;
    }

    function getEvent(uint256 index) public view returns (string memory, string memory, string memory, uint256) {
        require(index < events.length, "index out of range");
        FileEvent memory e = events[index];
        return (e.filename, e.ipfsHash, e.status, e.timestamp);
    }
}
