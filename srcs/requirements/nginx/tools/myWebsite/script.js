const operation = 
{
	fOperand : "",
	symbol : "",
	sOperand : "",
	result : NaN,
};

const upperScreen = document.querySelector(".upper-screen");
const lowerScreen = document.querySelector(".lower-screen");

//The handler must handle displaying the final result or the result of the previous operation
const handler = 
{
	set(target, prop, value)
	{
		if (prop === "symbol")
		{
			if (upperScreen.textContent.length === 21)
			{
				alert("Max amount of numbers exceeded");
				erase();
				return;
			}
			if (target[prop] == "")
			{
				target[prop] = value;
				target.fOperand === ""? upperScreen.textContent += ` ${value} ` : upperScreen.textContent = `${target.fOperand} ${value} `;
			}
			else
			{
				target.fOperand = operate(target);
				target[prop] = value;
				target.sOperand = "";
				upperScreen.textContent = `${target.fOperand} ${value} `
			}
		}
		else if (prop === "result")
		{
			if (target.fOperand === "" || target.symbol === "" || target.sOperand === "")
			{
				alert("Syntax Error");
				return ;
			}
			target[prop] = operate(target);
			if (Number.isFinite(target[prop]) === false)
			{
				alert("Syntax Error");
				erase();
				return ;
			}
			if (target[prop].toString().length > 12)
			{
				alert("Max amount of numbers exceeded");
				erase();
				return;
			}
			upperScreen.textContent = "";
			lowerScreen.textContent = target[prop];
			target.fOperand = parseFloat(target[prop]);
			target.symbol = "";
			target.sOperand = "";
		}
	},
};

const proxyOperation = new Proxy(operation, handler);

document.querySelector(".buttons").addEventListener("click", (e)=>
{
	if (e.target.classList.contains("btn-num"))
		processNum(e);
	else if (e.target.classList.contains("btn-symbol"))
		proccesOperator(e);
});


function operate(operation)
{
	if (operation.symbol === '+')
		return parseFloat((+operation.fOperand + +operation.sOperand).toFixed(2));
	else if (operation.symbol === '-')
		return parseFloat((+operation.fOperand - +operation.sOperand).toFixed(2));
	else if (operation.symbol === '*')
		return parseFloat((+operation.fOperand * +operation.sOperand).toFixed(2));
	else if (operation.symbol === '÷')
		return parseFloat((+operation.fOperand / +operation.sOperand).toFixed(2));
}

function processNum(e)
{
	if (upperScreen.textContent.length === 21)
	{
		alert("Max amount of numbers exceeded");
		erase();
		return;
	}
	if (isNaN(operation.result) === false && operation.fOperand !== "" && lowerScreen.textContent !== '0' && operation.symbol === "")
	{
		operation.fOperand = "";
		operation.result = NaN;
		lowerScreen.textContent = '0';
	}
	operation.symbol === "" ? operation.fOperand += e.target.textContent : operation.sOperand += e.target.textContent;
	operation.symbol === "" ? upperScreen.textContent += e.target.textContent : upperScreen.textContent += e.target.textContent;
}

function proccesOperator(e)
{
	const butn_symbol = 
	{
		operand : ['+', '-','*','÷'],
		negative : '±',
		clear : "AC",
		erase : "Del",
		dot : '.',
		equal : '='
	};
	if (butn_symbol.operand.includes(e.target.textContent) === true && proxyOperation.fOperand != "")
		proxyOperation.symbol = e.target.textContent;
	else if (butn_symbol.equal === e.target.textContent)
		proxyOperation.result = 0;
	else if (butn_symbol.clear === e.target.textContent)
		erase();
	else if (butn_symbol.dot === e.target.textContent)
		decimalPoint();
	else if (butn_symbol.negative === e.target.textContent)
		minusOperator();
	else if (butn_symbol.erase === e.target.textContent)
		deleteOperator();
}

function erase()
{
	operation.fOperand = "";
	operation.sOperand = "";
	operation.symbol = "";
	operation.result = NaN;
	upperScreen.textContent = "";
	lowerScreen.textContent = "0";
}

function decimalPoint()
{
	if (upperScreen.textContent.length === 21)
	{
		alert("Max amount of numbers exceeded");
		erase();
		return;
	}
	if (operation.fOperand !== "" && operation.sOperand === "" && operation.fOperand.includes('.') === false)
		operation.fOperand += '.';
	else if (operation.sOperand !== "" && operation.fOperand !== "" && operation.sOperand.includes('.') === false)
		operation.sOperand += '.';
	else
		return ;
	upperScreen.textContent += '.';
}

function minusOperator()
{
	if (operation.symbol === '' && Number.isFinite(parseFloat(operation.fOperand)) === true && operation.fOperand !== '0')
	{
		operation.fOperand = (parseFloat(operation.fOperand) * -1).toString();
		upperScreen.textContent = operation.fOperand;
	}
	else if (operation.symbol !== '' && Number.isFinite(parseFloat(operation.sOperand)) === true && operation.sOperand !== '0')
	{
		operation.sOperand = (parseFloat(operation.sOperand) * -1).toString();
		let sOperandsIndex = upperScreen.textContent.lastIndexOf(" ") + 1;
		upperScreen.textContent = upperScreen.textContent.substring(0, sOperandsIndex) + operation.sOperand;
	}
	if (upperScreen.textContent.length === 21)
	{
		alert("Max amount of numbers exceeded");
		erase();
		return;
	}
}

function deleteOperator()
{
	let lastIndex = upperScreen.textContent.length - 1;
	if (upperScreen.textContent[lastIndex] === ' ')
	{
		upperScreen.textContent = upperScreen.textContent.substring(0, lastIndex - 2);
		operation.symbol = "";
	}
	else if (operation.symbol === '' && operation.fOperand !== "")
	{
		upperScreen.textContent = upperScreen.textContent.substring(0, lastIndex);
		operation.fOperand = operation.fOperand.substring(0, lastIndex);
	}
	else if (operation.symbol !== '' && upperScreen.textContent[lastIndex] !== ' ')
	{
		upperScreen.textContent = upperScreen.textContent.substring(0, lastIndex);
		operation.sOperand = operation.sOperand.substring(0, operation.sOperand.length - 1);
	}
}