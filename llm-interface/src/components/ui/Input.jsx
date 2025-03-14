export const Input = ({ value, onChange, placeholder, disabled, className = '' }) => (
    <input
      type="text"
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      disabled={disabled}
      className={`
        w-full px-4 py-2 rounded-md border border-gray-300
        focus:outline-none focus:ring-2 focus:ring-blue-500
        disabled:bg-gray-100 disabled:cursor-not-allowed
        ${className}
      `}
    />
  );