var crypto = require('crypto');

const id = process.env.API_ID;
const key = process.env.KEY;

const preFix = "VERACODE-HMAC-SHA-256";
const verStr = "vcode_request_version_1";

var host = "api.veracode.com";

var hmac256 = (data, key, format) => {
	var hash = crypto.createHmac('sha256', key).update(data);
	// no format = Buffer / byte array
	return hash.digest(format);
}

var getByteArray = (hex) => {
	var bytes = [];

	for(var i = 0; i < hex.length-1; i+=2){
	    bytes.push(parseInt(hex.substr(i, 2), 16));
	}

	// signed 8-bit integer array (byte array)
	return Int8Array.from(bytes);
}

var getHost = () => {
	return host;
}

var generateHeader = (url, method) => {

	var data = `id=${id}&host=${host}&url=${url}&method=${method}`;
	var timestamp = (new Date().getTime()).toString();
	var nonce = crypto.randomBytes(16).toString("hex");

	// calculate signature
	var hashedNonce = hmac256(getByteArray(nonce), getByteArray(key));
	var hashedTimestamp = hmac256(timestamp, hashedNonce);
	var hashedVerStr = hmac256(verStr, hashedTimestamp);
	var signature = hmac256(data, hashedVerStr, 'hex');

	return `${preFix} id=${id},ts=${timestamp},nonce=${nonce},sig=${signature}`;
}

module.exports = {
	getHost,
	generateHeader
}