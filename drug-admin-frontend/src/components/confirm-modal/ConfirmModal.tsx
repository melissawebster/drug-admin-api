import './ConfirmModal.css'

interface ConfirmModalProps {
    message: string;
    onConfirm: () => void;
    onCancel: () => void;
}

const ConfirmModal: React.FC<ConfirmModalProps> = ({ message, onConfirm, onCancel }) => {
    return (
        <div className="modal-background">
            <div className="modal-box">
                <div className="modal-content">
                    <p>{message}</p>
                    <button onClick={onConfirm}>Sim</button>
                    <button onClick={onCancel}>Cancelar</button>
                </div>
            </div>
        </div>
    );
}

export default ConfirmModal;
