export const Card = ({ children, className = '' }) => (
    <div className={`bg-white shadow-lg rounded-lg ${className}`}>
      {children}
    </div>
  );
  
  export const CardHeader = ({ children }) => (
    <div className="px-6 py-4 border-b border-gray-200">
      {children}
    </div>
  );
  
  export const CardTitle = ({ children }) => (
    <h2 className="text-xl font-semibold text-gray-800">
      {children}
    </h2>
  );
  
  export const CardContent = ({ children }) => (
    <div className="p-6">
      {children}
    </div>
  );