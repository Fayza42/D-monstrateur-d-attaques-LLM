export const Button = ({ children, type = 'button', disabled, onClick, className = '' }) => (
    <button
      type={type}
      disabled={disabled}
      onClick={onClick}
      className={`
        px-4 py-2 rounded-md font-medium
        ${disabled 
          ? 'bg-gray-300 cursor-not-allowed' 
          : 'bg-blue-500 hover:bg-blue-600 text-white'}
        ${className}
      `}
    >
      {children}
    </button>
  );
