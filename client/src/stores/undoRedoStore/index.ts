import { computed, ref } from "vue";

import { defineScopedStore } from "@/stores/scopedStore";

import { LazyUndoRedoAction, UndoRedoAction } from "./undoRedoAction";

export { LazyUndoRedoAction, UndoRedoAction } from "./undoRedoAction";

export type UndoRedoStore = ReturnType<typeof useUndoRedoStore>;

export const useUndoRedoStore = defineScopedStore("undoRedoStore", () => {
    const undoActionStack = ref<UndoRedoAction[]>([]);
    const redoActionStack = ref<UndoRedoAction[]>([]);
    const maxUndoActions = ref(100);

    function $reset() {
        undoActionStack.value.forEach((action) => action.destroy());
        undoActionStack.value = [];
        clearRedoStack();
    }

    function undo() {
        flushLazyAction();
        const action = undoActionStack.value.pop();

        if (action !== undefined) {
            action.undo();
            redoActionStack.value.push(action);
        }
    }

    function redo() {
        const action = redoActionStack.value.pop();

        if (action !== undefined) {
            action.redo();
            undoActionStack.value.push(action);
        }
    }

    function applyAction(action: UndoRedoAction) {
        flushLazyAction();
        action.run();
        clearRedoStack();
        undoActionStack.value.push(action);

        while (undoActionStack.value.length > maxUndoActions.value && undoActionStack.value.length > 0) {
            const action = undoActionStack.value.shift();
            action?.destroy();
        }
    }

    function clearRedoStack() {
        redoActionStack.value.forEach((action) => action.destroy());
        redoActionStack.value = [];
    }

    /**
     * constructs a new action inline
     *
     * @example
     * action()
     *     .onRun(() => console.log("run"))
     *     .onUndo(() => console.log("undo"))
     *     .apply();
     */
    function action() {
        return new FactoryAction((action) => applyAction(action));
    }

    let lazyActionTimeout: ReturnType<typeof setTimeout> | undefined = undefined;

    /** action which is currently queued to run */
    const pendingLazyAction = ref<UndoRedoAction | null>(null);

    /**
     * Queues an action to be applied after a delay.
     * The action is applied immediately, should another action be applied, or be queued.
     * You can read the `pendingLazyAction` state, or `isQueued`, to find out if the action was applied.
     *
     * `flushLazyAction` runs the pending lazy action immediately.
     *
     * `setLazyActionTimeout` can be used to extend the timeout.
     *
     * @param action action to queue
     * @param timeout when to run the action in milliseconds. default to 1000 milliseconds
     */
    function applyLazyAction(action: LazyUndoRedoAction, timeout = 1000) {
        flushLazyAction();
        clearRedoStack();
        pendingLazyAction.value = action;
        action.queued();
        lazyActionTimeout = setTimeout(() => flushLazyAction(), timeout);
    }

    function clearLazyAction() {
        clearTimeout(lazyActionTimeout);
        pendingLazyAction.value = null;
    }

    function flushLazyAction() {
        clearTimeout(lazyActionTimeout);

        if (pendingLazyAction.value) {
            const action = pendingLazyAction.value;
            clearLazyAction();
            applyAction(action);
        }
    }

    function setLazyActionTimeout(timeout: number) {
        clearTimeout(lazyActionTimeout);
        lazyActionTimeout = setTimeout(() => flushLazyAction(), timeout);
    }

    const isQueued = computed(() => (action?: UndoRedoAction | null) => action && pendingLazyAction.value === action);

    const nextUndoAction = computed(() => undoActionStack.value[undoActionStack.value.length - 1]);
    const nextRedoAction = computed(() => redoActionStack.value[redoActionStack.value.length - 1]);

    const hasUndo = computed(() => Boolean(nextUndoAction.value));
    const hasRedo = computed(() => Boolean(nextRedoAction.value));

    const undoText = computed(() => {
        if (!nextUndoAction.value) {
            return "Nothing to undo";
        } else if (!nextUndoAction.value.name) {
            return "Undo";
        } else {
            return `Undo ${nextUndoAction.value.name}`;
        }
    });

    const redoText = computed(() => {
        if (!nextRedoAction.value) {
            return "Nothing to redo";
        } else if (!nextRedoAction.value.name) {
            return "Redo";
        } else {
            return `Redo ${nextRedoAction.value.name}`;
        }
    });

    return {
        undoActionStack,
        redoActionStack,
        maxUndoActions,
        undo,
        redo,
        applyAction,
        action,
        applyLazyAction,
        clearLazyAction,
        flushLazyAction,
        setLazyActionTimeout,
        isQueued,
        pendingLazyAction,
        nextUndoAction,
        nextRedoAction,
        undoText,
        redoText,
        hasUndo,
        hasRedo,
        $reset,
    };
});

class FactoryAction extends UndoRedoAction {
    private applyCallback: (action: FactoryAction) => void;

    private runCallback?: () => void;
    private undoCallback?: () => void;
    private redoCallback?: () => void;
    private destroyCallback?: () => void;

    constructor(applyCallback: (action: FactoryAction) => void) {
        super();
        this.applyCallback = applyCallback;
    }

    onRun(callback: typeof this.runCallback) {
        this.runCallback = callback;
        return this;
    }

    onUndo(callback: typeof this.undoCallback) {
        this.undoCallback = callback;
        return this;
    }

    onRedo(callback: typeof this.redoCallback) {
        this.redoCallback = callback;
        return this;
    }

    onDestroy(callback: typeof this.destroyCallback) {
        this.destroyCallback = callback;
        return this;
    }

    setName(name: string) {
        this.name = name;
        return this;
    }

    apply() {
        this.applyCallback(this);
    }

    run() {
        this.runCallback ? this.runCallback() : null;
    }

    undo() {
        this.undoCallback ? this.undoCallback() : null;
    }

    redo() {
        this.redoCallback ? this.redoCallback() : this.run();
    }

    destroy() {
        this.destroyCallback ? this.destroyCallback() : null;
    }
}
